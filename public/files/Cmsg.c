#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> // sleep/usleep

// Função para imprimir texto com efeito de digitação
void typeEffect(const char *texto, int velocidade) {
    while (*texto) {
        printf("%c", *texto);
        fflush(stdout);
        usleep(velocidade); // controla a velocidade
        texto++;
    }
}

int main() {
    int escolha;

    srand(time(NULL));
    escolha = (rand() % 10) + 1;

    printf("=====================================\n");
    printf("      GERADOR DE MENSAGENS EM C      \n");
    printf("=====================================\n\n");

    switch (escolha) {
        case 1:
            typeEffect("Confia no processo. Você ta evoluindo sem perceber.\n", 35000);
            break;
        case 2:
            typeEffect("Você é mais forte do que pensa. Continua.\n", 35000);
            break;
        case 3:
            typeEffect("Um passo por dia ainda é avanço.\n", 35000);
            break;
        case 4:
            typeEffect("Nada supera alguém que não desiste.\n", 35000);
            break;
        case 5:
            typeEffect("Orgulho do que você já conquistou até aqui.\n", 35000);
            break;
        case 6:
            typeEffect("Às vezes o progresso é silencioso. Mas existe.\n", 35000);
            break;
        case 7:
            typeEffect("Você não precisa ser perfeito, só constante.\n", 35000);
            break;
        case 8:
            typeEffect("O importante é começar — o resto você aprende no caminho.\n", 35000);
            break;
        case 9:
            typeEffect("Vai dar certo. Não tudo de uma vez, mas no tempo certo.\n", 35000);
            break;
        case 10:
            typeEffect("Seu futuro vai agradecer pelo esforço de hoje.\n", 35000);
            break;
        default:
            typeEffect("Ocorreu um erro inesperado.\n", 35000);
    }

    printf("\n=====================================\n");

    return 0;
}
