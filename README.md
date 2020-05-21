# zad 1

napisz funkcję, która przyjmuje dwa argumenty:

_arg1_ - string   
_arg2_ - lista stringów

funkcja ma wziąć stringa podanego w _arg1_ i wyciąć wszystkie wystąpienia wszystkich stringów w _arg2_ i zwrócić tak utworzony string.


Np.:
`abcdbabc_ac_ab_ca`, `[ab, ac]` -> `cdbc___ca`

# zad 2

stwórz klasę _Safe_ imitującą zachowanie sejfu.
Podczas tworzenia instancji tej klasy do konstruktora podajemy login i hasło.
Klasa ma zawierać:
1. metodę _open(login, password)_ 
1. metodę _save(login, password, new_object)_.

Metoda _open_ Powinna zwracać (w niemutowalnej postaci) zawartość sejfu po wywołaniu metody _open_ z poprawnym
(tj. zgodnym z tymi podanymi przy tworzeniu) loginem i hasłem. Zwróci False, jeśli login lub hasło są niepoprawne.   

Metoda _save_ powinna dodawać do zawartości sejfu obiekt podany jako _new_object_, jeżeli podane hasło i login są poprawne.
Zwróci False, jeśli login lub hasło są niepoprawne. 

Np.: 
```
safe = Safe("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy")
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", "abc")
safe.save("ArkadiuszNornica", "złehasło", "abc")  # zwraca False
safe.save("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy", 123)
print(safe.open("ArkadiuszNornica", "złehasło"))  # printuje False
print(safe.open("ArkadiuszNornica", "SzukamNornicyWMojejOkolicy"))  # printuje ("abc",123)
``` 

# zad 3

FizzBuzz
napisz funkcję, która przyjmuje liczbę i jeśli jest ona podzielna przez 3, zwraca "Fizz", jeśli jest podzielna przez 5, zwraca "Buzz", jeśli jest podzielna przez 3 i 5 zwraca "FizzBuzz", w przeciwnym przypadku zwraca samą liczbę.
```
for i in range(1, 21):
  print(fizzbuzz(i))
```
efekt:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

# DOMOWE:

## zadanie 4
Napisz własną funkcję liczącą wystąpienia podstringa w stringu __nie używając metody count__.

np.:
```
my_count("mam kota Mamrota co lubi jeść szprota", "ota")  # zwraca 3
```

## zadanie 5
Napisz skrypt, który wczytuje plik `zad03.txt` i tworzy listę obiektów _Cat_ na podstawie linijek pliku i ustawia w nich pola "name", "age", "color".

w efekcie można będzie zrobić:
```
... (wczytywanie pliku) ...
for cat in cats:
  print(cat.name, cat.age, cat.color)
```
wydrukuje:
```
Mruczek 6 bialy
Puszek Okruszek 12 czarny
Kardynal 21 zolty
Grumper 4 szary
```
__TIP__: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

## zadanie 6
Napisz funkcję, która

przyjmuję dwa argumenty:
1. lista stringów
1. string zawierający pojedynczą literę

zwraca listę stringów podaną jako argument pierwszy, ale te elementy listy, które kończą się na literę podaną jako argument drugi mają dodany suffix "_bingo"

np.:
```
bingify(["abc", "abca", "a", "cad", "baca", "bc"], "a")
```
zwraca:
```
["abc", "abca_bingo", "a_bingo", "cad", "baca_bingo", "bc"]
```
