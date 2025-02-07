queue = ["Matti", "Riikka", "Antti", "Jenni", "Anu", "Ville", "Jarno"]

'Time t + 1: The first person in the queue leaves after paying for their purchases'
queue.pop(0)
print(queue)

'Time t + 2: Ville recruits Anni to queue on his behalf.'
ville_recruit = queue.index('Ville')
queue.insert(ville_recruit,'Anni')
print(queue)

'Time t + 3: Jarno leaves, tired of the constant waiting.'
queue.remove('Jarno')
print(queue)

'Time t + 4: Marjo joins the end of the queue.'
queue.append('Marjo')
print(queue)

'Time t + 5: As a gentleman, Antti lets the two people behind him go ahead of him.'
antti = queue.index('Antti')
queue.insert(antti +2, queue.pop(antti))
print(queue)

'Is Jenni in the queue? If so, at what position? And who is the third last person in the queue?'
jenni = queue.index('Jenni')
+ 1 if 'Jenni' in  queue else None
count = queue[-3] if len(queue) >= 3 else None

print("Is Jenni in the queue?", "Yes" if "Jenni" in queue else "No")
print("Jenni's position:", jenni)
print("Third last person in the queue:", count)
