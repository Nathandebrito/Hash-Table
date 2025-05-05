Função de Hash: A função hashFunction é usada para calcular onde cada item vai ser armazenado, baseado em algo como o ID. Ela transforma o ID em um número que mostra onde o item deve ficar no array.

Resolução de Conflitos: Quando dois itens acabam na mesma posição, temos algumas maneiras de resolver isso:

    Encadeamento: No código, a gente cria uma lista de itens (itemList) para guardar todos os itens que caem na mesma posição de hash. Cada posição do array principal aponta para uma lista onde os itens são armazenados.
    
    Endereçamento Aberto: Embora o código não use isso, normalmente a gente procuraria outra posição disponível no array se a posição original estiver ocupada.

Essas técnicas ajudam a garantir que todos os itens sejam armazenados e recuperados corretamente, mesmo quando há conflitos.