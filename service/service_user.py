from repository.repository_user import RepositoryUser
from dto.dto_user import InputUser , InputLogin
from service import service_security

from fastapi import Depends, HTTPException

class ServiceUser :  
    def __init__(self, repository_user : RepositoryUser = Depends()) -> None : 
        self.repository_user = repository_user
        self.security_service = service_security
        
    def insert_new_user(self, new_user : InputUser) : 
        
        # Cek APakah ada duplikasi username
        is_duplicated = self.repository_user.find_userBy_username(new_user.username)
        if is_duplicated is not None : 
            raise HTTPException(status_code=400, detail="Username already exists")
        
        # Hash password sebelum disimpan    
        new_user.password = self.security_service.get_password_hash(
            new_user.password
        )
        return self.repository_user.insert_new_user(new_user) 
    
    def login_user(self, login: InputLogin) : 
        # periksa user 
        checkUser = self.repository_user.findUser_by_usernameNPassword(login)

        if checkUser is None : 
            raise HTTPException(status_code=404, detail="User Not Found")
        
        # Verifikasi Password 
        clearSecurity = self.security_service.verify_password(
            login.password,
            checkUser.password
        )

        if not clearSecurity : 
            raise HTTPException(status_code=401, detail="Invalid Password")

        return checkUser
        
        
    