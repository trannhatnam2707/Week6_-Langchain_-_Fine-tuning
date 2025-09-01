from chain import create_chain
from prompt import prompt

def main():
    chain = create_chain()

    #Nhập từ người dùng
    language = input("nhập ngôn ngữ bạn muốn học: ")

    #chạy chain 
    result = chain.run(language)

    print("Kết quả: ")
    print(result)

if __name__ == "__main__":
    main()

