FROM python:3.8-slim as dependency
WORKDIR /reqs
COPY requirements.txt /reqs
RUN pip install --no-cache-dir -r requirements.txt

FROM pedrochristo/pythonoracle
WORKDIR /home/app
COPY . .
RUN unzip -n <Wallet Name>.zip -d $TNS_ADMIN
COPY --from=dependency /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
CMD ["python","./DBTESTE.py"]
EXPOSE 5000