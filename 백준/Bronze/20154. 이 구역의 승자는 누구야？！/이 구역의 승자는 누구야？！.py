alpha = list("A B C D E F G	H I	J K	L M	N O	P Q R S T U V W	X Y	Z".split())
num = [3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
sumn = 0
for s in input():
    sumn += num[alpha.index(s)]
print("I'm a winner!" if sumn%2 else "You're the winner?")