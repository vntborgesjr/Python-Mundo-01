frase = 'Curso em Video Python'
print(frase[3])
print(frase[3:12])
print(frase[:12])
print(frase[13:])
print(frase[:15])
print(frase[1:15:2])
print(frase[::2])
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android')) # valor -1 significa que a string não existe
print('Curso' in frase)
print(frase.replace('Python', 'Android'))
print(frase.upper())
frase = frase.lower()
print(frase)
print(frase.lower().find('video'))
frase = frase.capitalize()
print(frase)
frase = frase.title()
print(frase)
frase = '     Aprenda Python   '
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
frase = 'Curso em Video Python'
print(frase.split())
frase = 'Curso em Video Python'.split
print(frase)
frase = 'Curso em Video Python'
frase = '-'.join(frase)
print(frase)
print(len(frase))
print(frase.find(' '))
print(frase.count(' '))
print(len(frase.split()[0]))
