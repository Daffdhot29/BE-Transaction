from repository.repository_user import RepositoryUser
from dto.dto_user import InputUser , InputLogin

from fastapi import Depends

class ServiceUser :  
    def __init__(self, repository_user : RepositoryUser = Depends()) -> None : 
        self.repository_user = repository_user

    def insert_new_user(self, new_user : InputUser) : 
        return self.repository_user.insert_new_user(new_user) 
    
    def login_user(self, login: InputLogin) : 
        return self.repository_user.findUser_by_usernameNPassword(login)

    