t1 = int(input("1r tamirchnii second="))
t2 = int(input("2r tarmirchnii second="))
t3 = int(input("3r tamirchnii second="))
niit = t1 + t2 + t3
minutes = niit // 60
seconds = niit % 60
print(f"{minutes}:{seconds:02d}")