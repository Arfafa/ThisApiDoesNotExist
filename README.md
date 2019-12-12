# Projeto
Projeto desenvolvido com o intuito de criar uma API não 
oficial para páginas: [this person does not exist](https://thispersondoesnotexist.com/image) 
e [this cat does not exist](https://thiscatdoesnotexist.com/) 

## Como Funciona?

### Instalação

```bash
$ pip install thisapidoesnotexist
```

### Demonstração

```python
from thisapidoesnotexist import get_person, get_cat

# Criando um objeto do tipo Person e um do tipo Cat
person = get_person()
cat = get_cat()

# Verificando as hashes das imagens coletadas
person.hash
cat.hash

# Salvando uma imagem no computador
person.save_image()

# Salvando imagem no computador com nome definido pelo programa
cat.save_image("gato.jpeg")

# Carregando novas imagens
person.new_image()
cat.new_image()
```
