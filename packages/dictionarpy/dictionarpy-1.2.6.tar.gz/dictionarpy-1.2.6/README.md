# DictionarPy

An extensible offline dictionary application

The dictionary comes prepopulated with a little over 53,000 words and 118,000
definitions available for offline reference. It is also designed to be
added to and grow with your lexicon.

### Some things you can do:

1. Add and remove words, parts of speech, definitions, IPA transcriptions
2. Show random words
3. Get similar words
4. Reference the built-in IPA key

### Statistics regarding this version's included dictionary:

```sh
$ dictionarpy -ns
Words:               53224
Definitions:         118657
IPA Transcriptions:  29812
Disk size:           10.49MB
──────────────────────────────────────────
Parts of speech:
    nom │ auxiliary verb │ intransitive verb
    │ nom masculin │ conjuction │ transitive
    verb │ plural noun │ preposition │ nom
    féminin │ adjective │ pronoun │ verb
    conjunction │ phrase │ article
    transitive/intransitive verb │ verbe
    noun │ interjection │ idiom
    abréviation │ adverb │ abbreviation
    determiner │ definite article
```

---

## Examples

- Add a word/definition to the database
  
  ```sh
  $ dpy -a -w "my new word" -p "my part of speech" -d "my definition!"
  ```

- Add or update the phonetic/phonemic transcription of a word

  ```sh
  $ dictionarpy -a -w "my new word" -i "/mj nu wɝd/"
  ```

- Show the definitions for a word (use `-n` to avoid ansi escape sequences)

  ```sh
  $ dictionarpy -n "my new word"                                                
  ┌──────────────────────┐
  │     my new word      │
  │     /mj nu wɝd/      │
  ├──────────────────────┤
  │ 1. my part of speech │
  │    my definition!    │
  └──────────────────────┘
  ```

- Remove a definition from the database

  ```sh
  $ dictionarpy -r 1 "my new word"
  ```

- Remove an entry from the database

  ```sh
  $ dictionarpy -R "remove_this_word"
  ```

- Learn a random word!

  ```sh
  $ dpy "$(dpy -z)"
  ```

For help and additional functionality: `dpy -h`
