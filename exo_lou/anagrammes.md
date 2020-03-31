# Présentation du problème
Une anagramme est un mot formé en permutant les lettres d’un autre mot. Ainsi, le mot "chien" est une anagramme
du mot "niche" tandis que "aube" est l’anagramme de "beau".

On se propose d’élaborer une fonction Anagrammes(Texte) permettant de détecter toutes les anagrames présentes
dans une chaîne de caractères. Par exemple, si l’on définit le texte

```python
text = "A Tanger, le gérant, sans argent, ne put acheter de grenat. Le maire" \
       " et Marie, à l'aube, lui en donnèrent un beau."
```
l’instruction ci-dessous

```
print(anagrams(text))
```
donnera lieu à l’affichage suivant :
```
[[’Le’,’le’], [’maire’, ’Marie’], [’aube’, ’beau’], [’Tanger’, ’gérant’, ’argent’, ’grenat’], [’ne’, ’en’]]
```
On voit sur l’exemple ci-dessus que le programme devra être capable de ne pas tenir compte de la casse (majuscule
/minuscule). Par exemple, la paire d’anagrammes "Marie" , "maire" devra être détectée. Le programme
devra également négliger les accents au sens suivant : certains mots dans Texte pourront comporter des accents,
mais dans la recherche d’anagrammes, ces accents seront supprimés. Ainsi, la paire d’anagrammes "gérant" et
"grenat" sera considérée comme valide.