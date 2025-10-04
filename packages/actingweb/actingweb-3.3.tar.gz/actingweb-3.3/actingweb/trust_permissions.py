"""
Trust Permission Storage for ActingWeb Unified Access Control.

This module manages per-trust-relationship permission storage using ActingWeb's
attribute store pattern. It allows individual trust relationships to override
the default permissions defined in trust types.
"""

import json
import logging
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict

from . import attribute
from . import config as config_class
from .constants import ACTINGWEB_SYSTEM_ACTOR, TRUST_PERMISSIONS_BUCKET

logger = logging.getLogger(__name__)


@dataclass
class TrustPermissions:
    """
    Per-trust-relationship permission overrides.
    
    These permissions override the base permissions defined in the trust type.
    Only specified fields will override - unspecified fields use trust type defaults.
    """
    
    actor_id: str  # The actor granting permissions
    peer_id: str   # The peer receiving permissions
    trust_type: str  # The trust type this relationship is based on
    
    # Permission overrides (None means use trust type default)
    properties: Optional[Dict[str, Any]] = None
    methods: Optional[Dict[str, Any]] = None
    actions: Optional[Dict[str, Any]] = None
    tools: Optional[Dict[str, Any]] = None
    resources: Optional[Dict[str, Any]] = None
    prompts: Optional[Dict[str, Any]] = None
    
    # Metadata
    created_by: str = "system"
    updated_at: Optional[str] = None
    notes: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TrustPermissions':
        """Create from dictionary loaded from storage."""
        return cls(**data)
    
    def get_permission_key(self) -> str:
        """Generate unique key for this trust relationship."""
        return f"{self.actor_id}:{self.peer_id}"
    
    def validate(self) -> bool:
        """Validate the trust permissions definition."""
        if not self.actor_id or not isinstance(self.actor_id, str):
            return False
        if not self.peer_id or not isinstance(self.peer_id, str):
            return False
        if not self.trust_type or not isinstance(self.trust_type, str):
            return False
        return True


class TrustPermissionStore:
    """
    Storage manager for per-trust-relationship permissions.
    
    Permissions are stored in actor-specific attribute buckets:
    bucket="trust_permissions", actor_id={actor_id}, name="{actor_id}:{peer_id}"
    
    This allows each actor to manage permissions for their trust relationships
    while maintaining the ActingWeb attribute store pattern.
    """
    
    def __init__(self, config: config_class.Config):
        self.config = config
        self._cache: Dict[str, TrustPermissions] = {}
        
    def _get_permissions_bucket(self, actor_id: str) -> Optional[attribute.Attributes]:
        """Get the trust permissions attribute bucket for an actor."""
        try:
            return attribute.Attributes(
                actor_id=actor_id,
                bucket=TRUST_PERMISSIONS_BUCKET,
                config=self.config
            )
        except Exception as e:
            logger.error(f"Error accessing trust permissions bucket for actor {actor_id}: {e}")
            return None
    
    def store_permissions(self, permissions: TrustPermissions) -> bool:
        """Store trust relationship permissions."""
        if not permissions.validate():
            logger.error(f"Invalid trust permissions definition: {permissions.get_permission_key()}")
            return False
        
        bucket = self._get_permissions_bucket(permissions.actor_id)
        if not bucket:
            logger.error(f"Cannot access trust permissions bucket for actor {permissions.actor_id}")
            return False
        
        try:
            # Store permissions data in attribute bucket
            permission_key = permissions.get_permission_key()
            permissions_data = permissions.to_dict()
            
            success = bucket.set_attr(
                name=permission_key,
                data=json.dumps(permissions_data)
            )
            
            if success:
                # Update cache
                cache_key = f"{permissions.actor_id}:{permissions.peer_id}"
                self._cache[cache_key] = permissions
                logger.info(f"Stored trust permissions: {cache_key}")
                return True
            else:
                logger.error(f"Failed to store trust permissions {permission_key}")
                return False
                
        except Exception as e:
            logger.error(f"Error storing trust permissions {permissions.get_permission_key()}: {e}")
            return False
    
    def get_permissions(self, actor_id: str, peer_id: str) -> Optional[TrustPermissions]:
        """Get trust relationship permissions."""
        cache_key = f"{actor_id}:{peer_id}"
        
        # Check cache first
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        bucket = self._get_permissions_bucket(actor_id)
        if not bucket:
            return None
        
        try:
            permission_key = f"{actor_id}:{peer_id}"
            
            # Get permissions from attribute bucket
            attr_data = bucket.get_attr(name=permission_key)
            
            if not attr_data or "data" not in attr_data:
                return None
            
            # Parse JSON and create TrustPermissions
            permissions_data = json.loads(attr_data["data"])
            permissions = TrustPermissions.from_dict(permissions_data)
            
            # Cache the result
            self._cache[cache_key] = permissions
            
            return permissions
            
        except Exception as e:
            logger.error(f"Error loading trust permissions {cache_key}: {e}")
            return None
    
    def list_actor_permissions(self, actor_id: str) -> List[TrustPermissions]:
        """List all permission overrides for an actor."""
        bucket = self._get_permissions_bucket(actor_id)
        if not bucket:
            return []
        
        permissions_list = []
        
        try:
            # Get all attributes from the trust permissions bucket
            bucket_data = bucket.get_bucket() or {}
            
            for attr_name, attr_info in bucket_data.items():
                try:
                    permissions_data = json.loads(attr_info["data"])
                    permissions = TrustPermissions.from_dict(permissions_data)
                    permissions_list.append(permissions)
                    
                    # Cache while we're at it
                    cache_key = f"{permissions.actor_id}:{permissions.peer_id}"
                    self._cache[cache_key] = permissions
                    
                except Exception as e:
                    logger.error(f"Error parsing trust permissions {attr_name}: {e}")
                    continue
            
            return permissions_list
            
        except Exception as e:
            logger.error(f"Error listing trust permissions for actor {actor_id}: {e}")
            return []
    
    def delete_permissions(self, actor_id: str, peer_id: str) -> bool:
        """Delete trust relationship permissions."""
        bucket = self._get_permissions_bucket(actor_id)
        if not bucket:
            return False
        
        try:
            permission_key = f"{actor_id}:{peer_id}"
            
            # Delete from attribute bucket
            success = bucket.delete_attr(name=permission_key)
            
            if success:
                # Remove from cache
                cache_key = f"{actor_id}:{peer_id}"
                self._cache.pop(cache_key, None)
                logger.info(f"Deleted trust permissions: {cache_key}")
                return True
            else:
                logger.error(f"Failed to delete trust permissions {permission_key}")
                return False
                
        except Exception as e:
            logger.error(f"Error deleting trust permissions {actor_id}:{peer_id}: {e}")
            return False
    
    def update_permissions(self, actor_id: str, peer_id: str, updates: Dict[str, Any]) -> bool:
        """Update specific permission fields for a trust relationship."""
        # Load existing permissions
        existing = self.get_permissions(actor_id, peer_id)
        if not existing:
            logger.error(f"Cannot update non-existent permissions for {actor_id}:{peer_id}")
            return False
        
        try:
            # Apply updates to the existing permissions
            updated_data = existing.to_dict()
            
            # Update only the specified fields
            for field, value in updates.items():
                if hasattr(existing, field):
                    updated_data[field] = value
                else:
                    logger.warning(f"Unknown permission field: {field}")
            
            # Create updated permissions object
            updated_permissions = TrustPermissions.from_dict(updated_data)
            
            # Store the updated permissions
            return self.store_permissions(updated_permissions)
            
        except Exception as e:
            logger.error(f"Error updating trust permissions {actor_id}:{peer_id}: {e}")
            return False
    
    def clear_cache(self):
        """Clear the internal cache."""
        self._cache.clear()


# Permission helper functions

def merge_permissions(base_permissions: Dict[str, Any], override_permissions: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merge base permissions with override permissions.
    
    Args:
        base_permissions: Default permissions from trust type
        override_permissions: Override permissions from trust relationship (can be None)
    
    Returns:
        Merged permissions dict
    """
    if not override_permissions:
        return base_permissions.copy()
    
    # Deep merge the permissions
    merged = base_permissions.copy()
    
    for category, overrides in override_permissions.items():
        if overrides is None:
            # None means use base permissions for this category
            continue
            
        if category in merged:
            if isinstance(merged[category], dict) and isinstance(overrides, dict):
                # Deep merge dictionaries
                merged[category] = {**merged[category], **overrides}
            else:
                # Replace with override
                merged[category] = overrides
        else:
            # Add new category
            merged[category] = overrides
    
    return merged


def create_permission_override(
    actor_id: str,
    peer_id: str,
    trust_type: str,
    permission_updates: Dict[str, Any]
) -> TrustPermissions:
    """
    Create a permission override object for a trust relationship.
    
    Args:
        actor_id: The actor granting permissions
        peer_id: The peer receiving permissions  
        trust_type: The trust type this relationship is based on
        permission_updates: Dict containing permission category updates
        
    Returns:
        TrustPermissions object ready for storage
    """
    # Extract permission categories from updates
    permissions = TrustPermissions(
        actor_id=actor_id,
        peer_id=peer_id,
        trust_type=trust_type,
        properties=permission_updates.get("properties"),
        methods=permission_updates.get("methods"),
        actions=permission_updates.get("actions"),
        tools=permission_updates.get("tools"),
        resources=permission_updates.get("resources"),
        prompts=permission_updates.get("prompts"),
        created_by=permission_updates.get("created_by", "system"),
        notes=permission_updates.get("notes")
    )
    
    return permissions


# Singleton instance
_permission_store: Optional[TrustPermissionStore] = None


def initialize_trust_permission_store(config: config_class.Config) -> None:
    """Initialize the trust permission store at application startup.""" 
    global _permission_store
    if _permission_store is None:
        logger.info("Initializing trust permission store...")
        _permission_store = TrustPermissionStore(config)
        logger.info("Trust permission store initialized")

def get_trust_permission_store(config: config_class.Config) -> TrustPermissionStore:
    """Get the singleton trust permission store (must be initialized first)."""
    global _permission_store
    if _permission_store is None:
        raise RuntimeError("Trust permission store not initialized. Call initialize_trust_permission_store() at application startup.")
    return _permission_store