## happy greet
* greet
  - utter_greet
  - utter_iamabot

## user info
* info
  - form_info
  - form{"name": "form_info"}
  - form{"name": null}
* affirm
  - utter_iamabot
  
## dafault fallback
* what_is_corona
  - action_custom_fallback

## Happy Path
* what_is_corona
  - utter_corona
* concern
  - utter_concern

## symptoms
* symptoms
  - utter_symptoms

## preventions
* prevention
  - utter_prevent

## happy vaccine
* Vaccination
  - utter_Vaccination
## happy incubation
* incubation
  - utter_incubation

## happy thanks
* thanks
  - utter_thanks

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
## how does corona spread
* corona_spread
  - utter_corona_spread
## corona food spread
* corona_food_spread
  - utter_corona_food_spread

## corona warm weather
* warm_weather
  - utter_warm_weather
## corona high risk
* high_risk
   - utter_high_risk
   
## world cases
* worldcases{"location": "London"}
  - slot{"location": "London"}
  - action_covid_country
  
## story 1
* worldcases
  - utter_ask_location
* worldcases{"location": "italy"}
  - slot{"location": "italy"}
  - action_covid_country
  
## email send
* email_addr{"EMAIL":"support@ineuron.ai"}
  - slot{"EMAIL":"support@ineuron.ai"}
  - action_send_email
  
## world cases
* world_data{"world": "global"}
  - slot{"world": "global"}
  - utter_worldmap
  - action_covid_world
  - utter_tell_email
* email_addr{"EMAIL":"support@ineuron.ai"}
  - slot{"EMAIL":"support@ineuron.ai"}
  - action_send_email

## demographic
* demo
  - utter_demograhic
  - utter_ask_state
* state_covid{"states": "delhi"}
  - slot{"states": "delhi"}
    - action_covid_state

## mograp
* demo
  - utter_demograhic
  - utter_ask_state
* state_covid{"states": "karnataka"}
  - slot{"states": "karnataka"}
    - action_covid_state
  
