"""
Things 3 Data Models

Pydantic models representing all Things 3 objects with validation,
serialization, and type safety.
"""

from datetime import datetime, date
from typing import Optional, List, Dict, Any, Union
from enum import Enum
from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict
from uuid import UUID


class ThingsStatus(str, Enum):
    """Todo status enumeration matching Things 3 AppleScript values"""
    OPEN = "open"
    COMPLETED = "completed"  
    CANCELED = "canceled"


class ThingsListType(str, Enum):
    """Things 3 list types"""
    INBOX = "Inbox"
    TODAY = "Today"
    UPCOMING = "Upcoming"
    ANYTIME = "Anytime"
    SOMEDAY = "Someday"
    LOGBOOK = "Logbook"
    TRASH = "Trash"
    PROJECT = "project"
    AREA = "area"


class ScheduleOption(str, Enum):
    """Schedule options for todos"""
    TODAY = "today"
    TOMORROW = "tomorrow"
    EVENING = "evening"
    ANYTIME = "anytime"
    SOMEDAY = "someday"
    THIS_WEEKEND = "this weekend"
    NEXT_WEEK = "next week"


class BaseThingsModel(BaseModel):
    """Base model for all Things 3 objects"""
    
    model_config = ConfigDict(
        # Allow field population by name or alias
        populate_by_name=True,
        # Use enum values in serialization
        use_enum_values=True,
        # Enable JSON schema generation
        json_schema_extra={
            "example": {}
        }
    )


class Tag(BaseThingsModel):
    """Things 3 tag model"""
    
    id: Optional[str] = Field(None, description="Unique tag identifier")
    name: str = Field(..., description="Tag name", min_length=1, max_length=100)
    parent_tag: Optional['Tag'] = Field(None, description="Parent tag for hierarchical tags")
    parent_tag_name: Optional[str] = Field(None, description="Parent tag name (alternative to parent_tag object)")
    keyboard_shortcut: Optional[str] = Field(None, description="Keyboard shortcut for the tag")
    
    @field_validator('name')
    @classmethod
    def validate_tag_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Tag name cannot be empty')
        return v.strip()
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "tag-123",
                "name": "work",
                "keyboard_shortcut": "w"
            }
        }
    )


class Contact(BaseThingsModel):
    """Things 3 contact model"""
    
    id: Optional[str] = Field(None, description="Unique contact identifier")
    name: str = Field(..., description="Contact name", min_length=1)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "contact-123",
                "name": "John Doe"
            }
        }
    )


class Area(BaseThingsModel):
    """Things 3 area of responsibility model"""
    
    id: Optional[str] = Field(None, description="Unique area identifier")
    name: str = Field(..., description="Area name", min_length=1, max_length=200)
    collapsed: bool = Field(False, description="Whether the area is collapsed in UI")
    tag_names: List[str] = Field(default_factory=list, description="Associated tag names")
    
    @field_validator('name')
    @classmethod
    def validate_area_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Area name cannot be empty')
        return v.strip()
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "area-123",
                "name": "Personal",
                "collapsed": False,
                "tag_names": ["life", "personal"]
            }
        }
    )


class Project(BaseThingsModel):
    """Things 3 project model (inherits from Todo)"""
    
    id: Optional[str] = Field(None, description="Unique project identifier")
    name: str = Field(..., description="Project name", min_length=1, max_length=200)
    notes: Optional[str] = Field(None, description="Project notes")
    area: Optional[Area] = Field(None, description="Associated area")
    area_name: Optional[str] = Field(None, description="Area name (alternative to area object)")
    contact: Optional[Contact] = Field(None, description="Assigned contact")
    status: ThingsStatus = Field(ThingsStatus.OPEN, description="Project status")
    
    # Dates
    creation_date: Optional[datetime] = Field(None, description="When project was created")
    modification_date: Optional[datetime] = Field(None, description="Last modification date")
    completion_date: Optional[datetime] = Field(None, description="When project was completed")
    cancellation_date: Optional[datetime] = Field(None, description="When project was canceled")
    activation_date: Optional[datetime] = Field(None, description="When project becomes active")
    due_date: Optional[date] = Field(None, description="Project deadline")
    
    # Tags
    tag_names: List[str] = Field(default_factory=list, description="Associated tag names")
    
    # Reminder functionality (Phase 1 & 2 implementation)  
    has_reminder: bool = Field(False, description="True if project has a specific reminder time set")
    reminder_time: Optional[str] = Field(None, description="Time component of reminder in HH:MM format")
    
    @field_validator('name')
    @classmethod
    def validate_project_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Project name cannot be empty')
        return v.strip()
    
    @model_validator(mode='after')
    def validate_dates(self):
        completion_date = self.completion_date
        cancellation_date = self.cancellation_date
        status = self.status
        
        # Validate status consistency with dates
        if status == ThingsStatus.COMPLETED and not completion_date:
            self.completion_date = datetime.now()
        elif status == ThingsStatus.CANCELED and not cancellation_date:
            self.cancellation_date = datetime.now()
        
        return self
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "project-123",
                "name": "Website Redesign",
                "notes": "Complete redesign of company website",
                "area_name": "Work",
                "status": "open",
                "due_date": "2024-03-01",
                "tag_names": ["work", "urgent"]
            }
        }
    )


class Todo(BaseThingsModel):
    """Things 3 todo model"""
    
    id: Optional[str] = Field(None, description="Unique todo identifier")
    name: str = Field(..., description="Todo title", min_length=1, max_length=500)
    notes: Optional[str] = Field(None, description="Todo notes")
    
    # Relationships
    project: Optional[Project] = Field(None, description="Associated project")
    project_name: Optional[str] = Field(None, description="Project name (alternative to project object)")
    area: Optional[Area] = Field(None, description="Associated area")
    area_name: Optional[str] = Field(None, description="Area name (alternative to area object)")
    contact: Optional[Contact] = Field(None, description="Assigned contact")
    
    # Status and completion
    status: ThingsStatus = Field(ThingsStatus.OPEN, description="Todo status")
    
    # Dates
    creation_date: Optional[datetime] = Field(None, description="When todo was created")
    modification_date: Optional[datetime] = Field(None, description="Last modification date")
    completion_date: Optional[datetime] = Field(None, description="When todo was completed")
    cancellation_date: Optional[datetime] = Field(None, description="When todo was canceled")
    activation_date: Optional[datetime] = Field(None, description="When scheduled todo becomes active")
    due_date: Optional[date] = Field(None, description="Todo deadline")
    scheduled_date: Optional[Union[date, str]] = Field(None, description="When todo is scheduled")
    
    # Tags
    tag_names: List[str] = Field(default_factory=list, description="Associated tag names")
    
    # Checklist
    checklist_items: List[str] = Field(default_factory=list, description="Checklist items")
    
    # Reminder functionality (Phase 1 & 2 implementation)
    has_reminder: bool = Field(False, description="True if todo has a specific reminder time set")
    reminder_time: Optional[str] = Field(None, description="Time component of reminder in HH:MM format")
    
    @field_validator('name')
    @classmethod
    def validate_todo_name(cls, v):
        if not v or not v.strip():
            raise ValueError('Todo name cannot be empty')
        return v.strip()
    
    @field_validator('scheduled_date')
    @classmethod
    def validate_scheduled_date(cls, v):
        if isinstance(v, str):
            # Validate schedule options
            valid_options = [opt.value for opt in ScheduleOption]
            if v.lower() not in valid_options:
                try:
                    # Try to parse as date
                    datetime.strptime(v, '%Y-%m-%d')
                except ValueError:
                    raise ValueError(f'Invalid schedule option: {v}. Use one of {valid_options} or YYYY-MM-DD format')
        return v
    
    @field_validator('reminder_time')
    @classmethod
    def validate_reminder_time(cls, v):
        """Validate reminder time format (HH:MM)."""
        if v is None:
            return v
            
        if not isinstance(v, str):
            raise ValueError('Reminder time must be a string in HH:MM format')
            
        # Validate HH:MM format
        try:
            if ':' not in v:
                raise ValueError('Reminder time must contain colon separator')
            
            parts = v.split(':')
            if len(parts) != 2:
                raise ValueError('Reminder time must be in HH:MM format')
                
            hour, minute = parts
            hour_int = int(hour)
            minute_int = int(minute)
            
            if not (0 <= hour_int <= 23):
                raise ValueError('Hour must be between 0 and 23')
            if not (0 <= minute_int <= 59):
                raise ValueError('Minute must be between 0 and 59')
                
            return v
            
        except (ValueError, TypeError) as e:
            if "invalid literal" in str(e).lower():
                raise ValueError('Reminder time must contain only numeric values')
            raise
    
    @model_validator(mode='after')
    def validate_relationships(self):
        project = self.project
        project_name = self.project_name
        area = self.area
        area_name = self.area_name
        
        # Ensure consistency between object and name fields
        if project and not project_name:
            self.project_name = project.name
        if area and not area_name:
            self.area_name = area.name
            
        # Can't be in both project and area
        if (project or project_name) and (area or area_name):
            raise ValueError('Todo cannot be in both a project and an area')
        
        return self
    
    @model_validator(mode='after')
    def validate_status_dates(self):
        completion_date = self.completion_date
        cancellation_date = self.cancellation_date
        status = self.status
        
        # Auto-set dates based on status
        if status == ThingsStatus.COMPLETED and not completion_date:
            self.completion_date = datetime.now()
        elif status == ThingsStatus.CANCELED and not cancellation_date:
            self.cancellation_date = datetime.now()
        elif status == ThingsStatus.OPEN:
            # Clear completion/cancellation dates for open todos
            self.completion_date = None
            self.cancellation_date = None
        
        return self
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "todo-123",
                "name": "Review quarterly report",
                "notes": "Check all financial figures and approve",
                "project_name": "Q4 Review",
                "status": "open",
                "due_date": "2024-01-15",
                "scheduled_date": "today",
                "tag_names": ["work", "urgent"],
                "checklist_items": ["Review revenue", "Check expenses", "Approve final version"],
                "has_reminder": True,
                "reminder_time": "14:30"
            }
        }
    )


class ThingsList(BaseThingsModel):
    """Things 3 list model (base for special lists like Today, Inbox, etc.)"""
    
    id: Optional[str] = Field(None, description="List identifier")
    name: str = Field(..., description="List name")
    list_type: ThingsListType = Field(..., description="Type of list")
    todo_count: int = Field(0, description="Number of todos in list")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "list-today",
                "name": "Today",
                "list_type": "Today",
                "todo_count": 5
            }
        }
    )


# Response Models for API operations
class TodoResult(BaseThingsModel):
    """Result model for todo operations"""
    
    success: bool = Field(..., description="Whether operation succeeded")
    message: str = Field(..., description="Human-readable message")
    todo: Optional[Todo] = Field(None, description="Todo object if applicable")
    todos: Optional[List[Todo]] = Field(None, description="List of todos if applicable")
    todo_id: Optional[str] = Field(None, description="Todo ID if applicable")
    error: Optional[str] = Field(None, description="Error code if failed")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional details")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Todo created successfully",
                "todo_id": "todo-123"
            }
        }
    )


class ProjectResult(BaseThingsModel):
    """Result model for project operations"""
    
    success: bool = Field(..., description="Whether operation succeeded")
    message: str = Field(..., description="Human-readable message")
    project: Optional[Project] = Field(None, description="Project object if applicable")
    project_id: Optional[str] = Field(None, description="Project ID if applicable")
    error: Optional[str] = Field(None, description="Error code if failed")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional details")


class AreaResult(BaseThingsModel):
    """Result model for area operations"""
    
    success: bool = Field(..., description="Whether operation succeeded")
    message: str = Field(..., description="Human-readable message")
    area: Optional[Area] = Field(None, description="Area object if applicable")
    area_id: Optional[str] = Field(None, description="Area ID if applicable") 
    error: Optional[str] = Field(None, description="Error code if failed")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional details")


# Update forward references
Tag.model_rebuild()
Project.model_rebuild()
Todo.model_rebuild()