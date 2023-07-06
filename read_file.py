log = []
with open('reviews.txt', 'r') as f:
    for line in f:
        log.append(line)

good_comment = []
for comment in log:
    if 'good' in comment:
        good_comment.append(comment)

print(len(good_comment))
