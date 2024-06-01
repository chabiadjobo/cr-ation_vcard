Convertisseur de Contacts en fichiers vCard

Ce script Python vous permet de convertir un fichier CSV nommé contacts.txt téléchargé depuis google contatc et contenant des contacts en fichiers vCard individuels. Les fichiers vCard peuvent être importés dans divers gestionnaires de contacts pour une utilisation facile.
Installation

    Assurez-vous d'avoir Python installé sur votre système. Vous pouvez le télécharger depuis python.org.
    Clonez ou téléchargez ce dépôt sur votre machine.

Utilisation

    Exportez vos contacts depuis votre application de gestion de contacts google sous forme de fichier CSV.
    Placez le fichier CSV dans le même répertoire que le script export_vcards.py.
    Ouvrez un terminal et naviguez jusqu'au répertoire contenant le script.
    Exécutez le script en utilisant la commande suivante :

    sh

    python export_vcards.py

    Les fichiers vCard seront créés dans un dossier nommé vcard et situé dans le même répertoire que le script Python.

Personnalisation

    Assurez-vous que les en-têtes dans votre fichier CSV correspondent aux champs utilisés dans le script.
    Vous pouvez modifier les champs utilisés dans le script selon vos besoins en adaptant la fonction create_vcard.

Remarques

    Assurez-vous que votre fichier CSV est encodé en UTF-8 pour éviter les problèmes de caractères.
    En cas de caractères non valides dans les noms de fichiers, le script nettoie automatiquement les noms de fichiers en supprimant les caractères spéciaux.

Contributions

Les contributions sous forme de rapports de bogues, d'améliorations de fonctionnalités ou de suggestions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.
Licence

Ce projet est sous licence MIT. Pour plus d'informations, consultez le fichier LICENSE.