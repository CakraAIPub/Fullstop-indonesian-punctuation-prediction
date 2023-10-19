# Fullstop-indonesian-punctuation-prediction

This model predicts the punctuation of Indonesian languange. It has been created to restore punctuation of transcribed from speech recognition models.
This model Based on the work https://github.com/oliverguhr/fullstop-deep-punctuation-prediction

The model restores the following punctuation markers: **"." "," "?" "-" ":"**

**Hugging Face** : https://huggingface.co/Rizkinoor16/fullstop-indonesian-punctuation-prediction

## Install 

To get started install the package from [pypi](https://pypi.org/project/deepmultilingualpunctuation/):

```bash
pip install deepmultilingualpunctuation
```
### Restore Punctuation
```python
from deepmultilingualpunctuation import PunctuationModel

model = PunctuationModel("Rizkinoor16/fullstop-indonesian-punctuation-prediction")
text = "halo bagaimana kabarmu"
result = model.restore_punctuation(text)
print(result)
```
**output**
> halo, bagaimana kabarmu?


## Results
```
      precision    recall  f1-score   support 

           0       0.98      0.99      0.98  
           .       0.89      0.91      0.90   
           ,       0.84      0.79      0.81   
           ?       0.84      0.79      0.82   
           -       0.96      0.90      0.93    
           :       0.91      0.89      0.90   

    accuracy                           0.97  
   macro avg       0.90      0.88      0.89    
weighted avg       0.97      0.97      0.97  
```

## Contact

Rizki Noor <rizki@cakra.ai>

**Linkedin** : [Noor Muhamad Rizki](https://www.linkedin.com/in/noor-muhamad-rizki-114600231/)
