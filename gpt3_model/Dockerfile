FROM python:3.8-slim-buster

ENV HOST='hb_model'
ENV PORT='1240'

#EXPOSE 1240

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install torch==1.8.0+cpu torchvision==0.9.0+cpu torchaudio===0.8.0 -f https://download.pytorch.org/whl/torch_stable.html

ADD /hb_model.tar.gz .
COPY generate_transformers.py .

CMD python generate_transformers.py --model_type=gpt2 --model_name_or_path=./hb_model --k=5 --p=0.95 --length=200