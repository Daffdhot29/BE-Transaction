from passlib.context import CryptContext 

# Inisialisasi CryptContext dengan algoritma hashing 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fungsi untuk verifikasi password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    
# Fungsi untuk hash password
def get_password_hash(password):
    return pwd_context.hash(password)

