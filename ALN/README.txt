Para executar o código de forma que erros não sejam recorrentes, deve-se instalar corretamente as bibliotecas utilizadas:

os -> pip install os-sys 
random -> pip install random2
cv2 -> pip install opencv-python
numpy -> pip install numpy
pandas -> pip install pandas
sklearn.decomposition -> pip install -U scikit-learn

Após a instalação dessas dependências é fundamental a verificação se o arquivo .py desse trabalho se encontra na mesma pasta contendo a pasta recdev-master ou, caso não esteja, realizar a atualização nas variáveis paths e caminhoBonus para o endereço onde a pasta recdev-master e suas subpastas estarão localizadas.

Com esses requisitos atendidos, basta alterar a dificuldade dos testes a partir da posição do path na chamada das funções. Para os testes das bases de dados oferecidas, aualiza-se as chamadas presentes nas linhas 156 e 157. 

Para realização do teste com a presença das imagens de dificuldade hard somadas a imagens alteradas, como imagens com a adição de óculos nas pessoas, utiliza-se a função TesteBonus presente nas linhas 160 e 161.

Além desses fatores, se atentar na extensão dos arquivos de imagem, que podem ser alterados nas linhas 111 e 131.