import os
import pwd

word: str = "From: "
Path: str = f'/Users/{pwd.getpwuid(os.getuid())[0]}/Desktop/Email_extractor-main/eml/'
filelist = os.listdir(Path)

for file in filelist:
    if file.endswith(".eml"):
         with open(Path + file, 'r') as f:
            for i in f.readlines():
                if word in i:
                    result = i.replace("From: ", '').replace('>', '').replace('<', '').strip().split(' ')
                    email = result[len(result) - 1]
                    o = open('emails.csv', 'a')
                    o.write(f'{email}\n')
