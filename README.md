# Bia
## Assistente de LIBRAS (linguagem brasileira de sinais)

A Bia compreende qual algarismo em libras está sendo realizado diante à webcam. 

## Dependências
Você precisa instalar o opencv via pip
```sh
pip install opencv-python
```
Caso existam problema ao instalar o ```opencv-python```, por favor, cheque este [link](https://pypi.org/project/opencv-python/)  

## Como contribuir

A aplicação está parecida com os componentes de uma aplicação ```React```.  
Você pode criar uma nova página vide exemplos no próprio código.  
Desenvolva uma página no diretório ```pages``` e link a nova página na aplicação adicionando uma rota na classe ```app```. Verifique o arquivo ```app.py``` para mais exemplos.

Se você deseja adicionar novas frameworks, não esqueça de atualizar o ```readme``` e empacotar no pacote ```Bia```.

## Como rodar

Para treinar a deep learning:
```python App.py```
Para deixar a DL tentar adivinhar qual digito você está mostrando:( ainda não está funcionando)
```python predict.py```

## Considerações finais

Fase de desenvolvimento. O bot não está concluído.
