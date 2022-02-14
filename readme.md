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
* Add continent (Future feature)


### Create a basic api 

```
/trivia/captial
```

Eventuall will have a basic trivia api that can call both capitals and
landmarks as well as everything else.




## resources

* State capital
  <https://github.com/jasperdebie/VisInfo/blob/master/us-state-capitals.csv>

* World capitals
  <https://raw.githubusercontent.com/icyrockcom/country-capitals/master/data/country-list.json>

## TODO:

* Restrucure django apps, should have an api with urls like /api/capitals/
* Add frontend to django app with vvery simple webpage showing how to use api

## Structure

Yes it's insane and crazy to do it this way, I know that the data should be
stored in a database and I know that the api functions should be within the
django strucure, oh well - I like it this way.



### Create new questions

Follow the existing fomrat, then just copy the script and it should work.





