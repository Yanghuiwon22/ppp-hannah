import requests
# import 는 불러오는거 (빨간줄은 무슨이야기인줄 모르겠다. install이 필요하다.)

def main():
    URL = "https://sobi.chonbuk.ac.kr/function/ajax.get.rest.data.php"
    # 인터넷 접속만 된다면 어디서든 파일을 열 수 있다.
    data = {"code": "mobile1"}
    # 코딩과 상관없음 (진수원,    ,     )세 가지중 첫번째 데이터라는 뜻
    with open("./cafeteria_menu.html", "w", encoding="UTF-8") as f:
    # 파일네임(), "w" => "r"은 안써도 되지만 W는 꼭 써야 함(파일을 사용하기 위해서 작성), 데이터가 글자를 처리할 때(한글을 저장하기 위해서)
        res = requests.post(URL, data=data)
        # 포스트방식과 get 방식 (웹에 접속해서 데이터를 가져오기 위해서)
        res.encoding = "UTF-8"
        f.write(res.text)
#       웹의 데이터를 파일로 저장하기 위하여 작성


if __name__=="__main__":
    main()