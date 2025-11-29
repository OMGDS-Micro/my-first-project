import random
import string

def generate_password(length=12):
    """隨機生成一個包含大小寫字母和數字的密碼"""
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# 執行程式並生成一個 16 個字元的密碼
if __name__ == "__main__":
    new_password = generate_password(16)
    print(f"生成的密碼: {new_password}")
    print("注意：密碼長度為 16 個字元。")
