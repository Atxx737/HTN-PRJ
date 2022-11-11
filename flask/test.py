from werkzeug.security import generate_password_hash, check_password_hash

hashed_password = generate_password_hash('admin')

print(check_password_hash(hashed_password, 'admin')) # prints True
print(check_password_hash(hashed_password, 'foobarbaz')) # prints False