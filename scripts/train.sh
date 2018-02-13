#!/bin/bash
curl -i --user "b8c9ab8b-278e-49c9-bc41-309ce83a7612":"RdCKtar5NO7O" -F training_data=@./meetup_bio_data -F training_metadata="{\"language\":\"en\",\"name\":\"journeyboiyenlc-natural-la-1517526315633\"}" "https://gateway.watsonplatform.net/natural-language-classifier/api/v1/classifiers" 
