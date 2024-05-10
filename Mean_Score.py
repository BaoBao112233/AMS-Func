name = input("Nhập tên học sinh: ")
score_van = float(input("Nhập điểm văn: "))
score_toan = float(input("Nhập điểm toán: "))
score_anh = float(input("Nhập điểm anh: "))
mean_score = (score_van + score_anh + score_toan)/3
print("Học sinh "+ name + " có điểm số trung bình là: " + str(mean_score))