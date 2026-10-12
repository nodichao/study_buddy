# Study Buddy

Study Buddy est un assistant d'étude en ligne de commande. Il utilise l'API
Mistral pour répondre aux questions de l'utilisateur avec une personnalité
amicale, patiente et pédagogique.

## Fonctionnalités

- Explications simples et progressives.
- Ton encourageant et adapté à l'apprentissage.
- Conservation de l'historique de la conversation.
- Détection des questions vides.
- Commandes `quit`, `exit` et `stop` pour quitter l'application.
- Paramètres facilement modifiables : modèle, créativité et longueur des réponses.

## Prérequis

- Python 3.10 ou une version plus récente.
- Un compte Mistral AI Studio avec un accès API actif.
- Une clé API Mistral.

L'accès à l'API peut nécessiter la validation des informations de paiement dans
la console Mistral, même si certains services Mistral proposent une offre
gratuite.

## Installation

Depuis le dossier du projet, installez les dépendances :

```powershell
pip install mistralai python-dotenv
```

## Configuration de la clé API

Créez un fichier `.env` à la racine du projet :

```env
MISTRAL_API_KEY=votre_cle_api_mistral
```

Ne partagez jamais ce fichier et ne publiez pas votre clé API dans un dépôt
GitHub. Ajoutez `.env` à votre fichier `.gitignore` si nécessaire :

```gitignore
.env
```

## Lancement

Exécutez le programme avec :

```powershell
python study_buddy.py
```

Saisissez ensuite votre question. Pour fermer l'assistant, écrivez :

```text
quit
```

Vous pouvez aussi utiliser `exit` ou `stop`.

## Paramétrage

Les réglages se trouvent au début de
[study_buddy.py](./study_buddy.py) :

```python
MODEL = "ministral-8b-2512"
TEMPERATURE = 0.3
MAX_TOKENS = 500
```

### Modèle

`MODEL` définit le modèle Mistral utilisé. Remplacez sa valeur par un nom de
modèle disponible pour votre compte.

### Créativité

`TEMPERATURE` contrôle la variation des réponses :

- `0.0` à `0.3` : réponses plus précises et stables ;
- `0.4` à `0.7` : réponses plus naturelles ;
- `0.8` à `1.0` : réponses plus créatives.

Pour un assistant scolaire, une valeur autour de `0.3` est généralement adaptée.

### Longueur

`MAX_TOKENS` limite la longueur maximale d'une réponse. Augmentez cette valeur
pour obtenir des explications plus détaillées.

### Personnalité

La personnalité et la méthode pédagogique sont définies dans la variable
`SYSTEM_PROMPT`. Vous pouvez y préciser :

- le niveau scolaire de l'utilisateur ;
- la langue des réponses ;
- le ton souhaité ;
- l'utilisation d'exemples, d'étapes ou de questions-guides.

## Résolution des problèmes

### Erreur `429` ou `Rate limit exceeded`

Cette erreur signifie que l'API a refusé la requête à cause d'une limite de
quota, de crédits ou de débit. Vérifiez dans la console Mistral :

- que l'accès API est activé ;
- que les informations de paiement sont validées si nécessaire ;
- que le compte dispose encore de crédits ;
- que la clé API utilisée est bien celle du compte actif ;
- que le modèle choisi est disponible pour ce compte.

### Clé API absente

Vérifiez que le fichier `.env` se trouve bien dans le dossier du projet et que
la variable s'appelle exactement `MISTRAL_API_KEY`.

## Sécurité

- Ne mettez jamais votre clé API directement dans le code.
- Ne partagez pas votre fichier `.env`.
- Si une clé est exposée, révoquez-la immédiatement dans la console Mistral et
  créez-en une nouvelle.
