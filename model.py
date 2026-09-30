
from datetime import datetime
from pydantic import BaseModel
from typing import Literal


# representation of data collected from a reddit post
class Post(BaseModel):
    id: str
    author: str
    title: str
    date_posted: datetime
    raw_post: str
    upvotes: int
 
 
# representation of data collected from a comment under a reddit post
class Comment(BaseModel):
    id: str
    
    # Identifies the post the comment is under
    source_id: str
    
    author: str
    date_posted: datetime
    upvotes: int
#   source: Post.id 
 

class Evidence(BaseModel):
    # Identifies whether the evidence is from a reddit post or comment
    source_type: Literal["post", "comment"]
    
    source_id: str
    specific_evidence: str
    
   
# Representation of a USE CASE identified by agent after analysis on reddit posts and comments
class Usecase(BaseModel):
    title: str
    description: str
    evidence: list[Evidence]
    

# Representation of a GAP identified by agent after analysis on reddit posts and comments
class Gap(BaseModel):
    title: str
    description: str
    count: int
    evidence: list[Evidence]
    date_first_seen: datetime
    
