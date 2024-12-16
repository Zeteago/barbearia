Tema : Agenda Moderna para Barbearia e Salão

Objetivo do Projeto:
	Facilitar, melhorar e dar mais segurança ao Barbeiro e a Cabelereira quando vão marcar os horários do clientes.

Delimitação do Problema:
	(Ponto central do projeto) Os dados não podem se perder facilmente, como por exemplo uma falha no Wi-Fi ou dados móveis.

Justificativa da Escolha do Tema:
	O meu barbeiro, junto de sua mulher, comentou com meu pai que já havia acontecido mais de uma vez o problema de chegarem 2 clientes no mesmo horário por sua agenda não te salvo os dados. Eu precisava de experiência, estava no 2° ano do Ensino Médio, cursando Desenvolvimento de Sistemas na ETEC Professora Terezinha Monteiro dos Santos, e no próximo ano já era meu TCC (Trabalho de Conclusão de Curso). Quando iniciei esse projeto, já havia se passado metade do ano de 2024, ou seja se eu quisesse ter 1 ano para realizar o meu TCC, eu precisaria completar esse projeto em 6 meses!

Método de Trabalho: 
	Como eu queria ganhar experiência com este projeto eu resolvi escolher a melhor biblioteca ou framework de base para o app, o que me serviu melhor foi o FLET, pois esse framework faz com que seu código possa ser tanto um arquivo para Desktop, Mobile (IOS e Android) como um Site! Após a escolha da biblioteca eu precisei pensar no design do aplicativo, e essa parte foi demorada (4 meses). Em seguida escolhi fazer de forma Procedural e Estruturada o código, pois POO seria mais eficiente, mas não daria tempo, eu teria que aprender a mexer melhor com POO e isso levaria mais tempo. Por último, o banco de dados que escolhi, o SQLite3, pois é offline, ele salva os arquivos localmente, e não tem risco de perder dados.

Organização do Trabalho:
	Design -> Tipo do código -> Banco de dados

Descrição Geral do Sistema:
	O aplicativo num todo tem 6 telas -> Tela Principal, Tela Edição, Tela Adicionar, Tela Pesquisa, Tela Relatório, Tela Relatórios.
	Hierarquia de funções:
		Código limpo ->      Função Semana;
						Main ->
							Necessário; *(CONEXÃO)*
							Screen Main; *(CONEXÃO)*
							Fechar diálogo;
							Excluir; *(CONEXÃO)*
							Confirmação;
							Função Voltar;
							Tirar;
							Pesquisar -> *(CONEXÃO)*
								Remover Acentos;
							Avançar;
							Retroceder;
							Muda Dia;
							Editar; *(CONEXÃO)*
							Mascara;
							Tela Adiciona ->
								Mudou Data;
								Voltar;
								Escolher Hora ->
									On_Time_Confirm;**
								Fechar_Dialogo;
								Fechar Dialogo e Adicionar;
								Verifica; *(CONEXÃO)*
								Adicionar; *(CONEXÃO)*
								Screen;
							Adicionar;
							Tela Editar -> *(CONEXÃO)*
								Fechar Dialogo e Excluir;
								Fechar Dialogo da Hora;
								Fechar Dialogo e Adicionar;
								Alterar; *(CONEXÃO)*
								Verifica; *(CONEXÃO)*
								Mudou Data;
								Voltar;
								Screen Edit;
				 
			




