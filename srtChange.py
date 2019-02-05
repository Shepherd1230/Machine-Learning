#这是一个将srt字幕转换成文稿的小程序
#主要用来学习youtube上面各种各样的英文课程
# 同时也方便做笔记


filename = '(English)Lecture 8 _ Deep Learning Software - YouTube.srt'

subtitle=open('MySubtitle.srt','w',encoding='utf-8')

with open(filename, encoding='UTF-8') as file_obj:
    for line in file_obj:
        line = line.strip()
        if len(line) and not line.isdigit():
            first_str = line[0:2]
            if not first_str.isdigit():
                print(line)
                subtitle.write(line)

subtitle.close()
