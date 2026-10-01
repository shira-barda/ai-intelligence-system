
from datetime import datetime
from pydantic import BaseModel, Field, field_validator
from typing import Literal


# ---------------------
# Reddit/Source Data
# ---------------------

# Representation of data collected from a reddit post
class Post(BaseModel):
    id: str = Field(min_length = 1)                     # Obtained from reddit
    author: str
    title: str
    date_posted: datetime
    raw_post: str
    upvotes: int
    
    @field_validator('id')                              # Validates Post ID
    @classmethod
    def validate_post_id(cls, v: str) -> str:
        n : int = 0
        for char in v:                                  # ID must only contain alphanumeric characters
            if not(char.isalnum()):
                n += 1    
        if n > 0:
            raise ValueError('ID must be strictly alphanumeric')
        
        return v

    @field_validator('raw_post')                        # Validates raw POST
    @classmethod
    def validate_source_text(cls, v: str) -> str:
        if v.strip() == "":                             # No string of whitespace or empty string
            raise ValueError('Post is empty')
        
        n : int = 0
        for char in v:                                  # Must have at least 1 letter or number
            if char.isalnum():
                n += 1    
        if n <= 0:
            raise ValueError('Post contains no meaningful characters')
        
        if len(v) < 70:                                 # Must be long enough to contain meaningful information (at least a sentence long)
            raise ValueError('Post (likely?) doesn\'t contain meaningful information')
        
        return v
 
 
# Representation of data collected from a comment under a reddit post
class Comment(BaseModel):
    id: str = Field(min_length = 1)                     # Obtained from reddit
    source_id: str = Field(min_length = 1)              # Identifies the post the comment is under
    author: str
    date_posted: datetime
    upvotes: int
    raw_comment: str

    @field_validator('id', 'source_id')                 # Validates Post ID
    @classmethod
    def validate_post_id(cls, v: str) -> str:
        n : int = 0
        for char in v:                                  # ID must only contain alphanumeric characters
            if not(char.isalnum()):
                n += 1    
        if n > 0:
            raise ValueError('ID must be strictly alphanumeric')
        
        return v
        
    @field_validator('raw_comment')                     # Validates raw COMMENT
    @classmethod
    def validate_source_text(cls, v: str) -> str:
        if v.strip() == "":                             # No string of whitespace or empty string
            raise ValueError('Comment is empty')
        
        n : int = 0
        for char in v:                                  # Must have at least 1 letter or number
            if char.isalnum():
                n += 1    
        if n <= 0:
            raise ValueError('Comment contains no meaningful characters')
        
        # TODO: Add content validator for comments
                
        return v
 


# ---------------------
# Evidence
# ---------------------

# Describes information supporting Use Case, Gap, New Technology, and Trend claims
class Evidence(BaseModel):
    source_type: Literal["post", "comment"]             # Identifies source as Reddit Post or Comment
    source_id: str = Field(min_length = 1)              # Post or Comment ID
    specific_evidence: str
    
    
  
# ---------------------
# Synthesized Data
# ---------------------

 
# Representation of a USE CASE identified by agent after analysis on reddit posts and comments
class Usecase(BaseModel):
    title: str                                          # TODO: Add field validator
    description: str                                    # TODO: Add field validator
    evidence: list[Evidence] = Field(min_length = 1)
    

# Representation of a GAP identified by agent after analysis on reddit posts and comments
class Gap(BaseModel):
    title: str                                          # TODO: Add field validator
    description: str                                    # TODO: Add field validator
    occurrence_count: int = Field(ge=0)
    evidence: list[Evidence] = Field(min_length = 1)
    date_first_seen: datetime
    

# TODO: Define NEW TECHNOLOGIES

class NewTechnology(BaseModel):
    pass

# TODO: Structure TRENDS

class Trend(BaseModel):
    pass
