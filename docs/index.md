![Logotipo do projeto](assets/astrop.png){width="300" .center}
# Notas musicais

## Como usar

Você pode chamar as escalas via linha de comando. Por exemplo:

```powershell
poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ F │ G  │ A   │ A# │ C │ D  │ E   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração da tônica da escala

O primeiro parâmetro do CLI é a tônica da escala que deseja exibir. Desta forma, você pode alterar a escala retornada. Por exemplo, a escala de F#

```powershell
poetry run escalas F#
```

### Alteração da tonalidade
Para alterar a tonalidade, utiliza-se o segundo parâmetro. Por exemplo, a escala de `D# maior`

```powershell
poetry run escalas D# maior

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

## Mais informações
Para mais informações sobre a utilização do CLI, utilize a flag `--help`