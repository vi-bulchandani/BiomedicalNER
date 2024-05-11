from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoConfig, AutoModelForTokenClassification, AutoModel

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")
tokenizer.save_pretrained('/workspace/amit_ug/rohit/bert-base-uncased/tokenizer')

model = AutoModel.from_pretrained("google-bert/bert-base-uncased")
model.save_pretrained('/workspace/amit_ug/rohit/bert-base-uncased/model')