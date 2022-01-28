 A trivia app


## routes

Question
category

## categories


Captial cities
    * Of US states
    * Of Europe
    * Africa
    * Of Americas
    * Asia

Countries

Flags

General Knowlege

Famous Landmarks (ken)


### return (json)

Question
Answer
LIst of wrong answers (including the answer, abcd)
Optional image


## Full example of what we want

* General Knowledge
```
curl example.com/api/trivia?cat=1

{
question: 'what is the best energy drink',
answer: 'monster'
choices: '['monster','lucazade','water','red bull']
}

```

* Cities

```
curl example.com/api/trivia?cat=2

{
question: 'What is the capital of the UK',
answer: 'London'
choices: '['london','Amsterdam','Kiev','Helsinki']
}
```

## TODO

* Captial cities
* list of landmarks

### Create the function to generate the captial cities question 


* genrate question ✅
* Fix relative path
* Add continent (Future feature) [x]


### Create a basic api 





## resources

* State capital
  <https://github.com/jasperdebie/VisInfo/blob/master/us-state-capitals.csv>

* World capitals
  <https://raw.githubusercontent.com/icyrockcom/country-capitals/master/data/country-list.json>







