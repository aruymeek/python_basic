command_message = ''' \n 작업 명령어를 입력해주세요. (종료: EXIT)
# 등록 (영화:  1, 감독:  2, 배우:  3)
# 삭제 (영화: 11, 감독: 12, 배우: 13)
# 조회 (영화: 21, 감독: 22, 배우: 23)

'''


# 데이터
movies = {
    'MOV001': ['인셉션', 2010, '미국'],
    'MOV002': ['뷰티인사이드', 2015, '한국'],
    'MOV003': ['어벤져스 4', 2019, '미국'],
    'MOV004': ['트롤', 2020, '미국'],
    'MOV005': ['기생충', 2019, '한국'],
}

directors = {
    'DIR001': ['MOV001', '크리스토퍼 놀란'],         
    'DIR002': ['MOV002', '백종열'],
    'DIR003': ['MOV003', '안소니 루소'],
    'DIR004': ['MOV003', '조 루소'],
    'DIR005': ['MOV004', '월트 도른'],
    'DIR006': ['MOV004', '데이빗 P. 스미스'],
    'DIR007': ['MOV005', '봉준호']
}

actors = {
    'ACT001': ['MOV001', '레오나르도 디카프리오', 1974],   
    'ACT002': ['MOV002', '한효주', 1987],
    'ACT003': ['MOV002', '박서준', 1988],
    'ACT004': ['MOV002', '유연석', 1984],
    'ACT005': ['MOV003', '로버트 다우니 주니어', 1965],
    'ACT006': ['MOV003', '베네딕트 컴버배치', 1976],
    'ACT007': ['MOV003', '스칼렛 요한슨', 1984],
    'ACT008': ['MOV004', '안나 켄드릭', 1985],
    'ACT009': ['MOV005', '송강호', 1967],
    'ACT010': ['MOV005', '최우식', 1990]
}