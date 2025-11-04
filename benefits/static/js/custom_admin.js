// Aguarda o carregamento completo do DOM (Document Object Model) para executar todos os scripts
document.addEventListener('DOMContentLoaded', function() {

    // --- Ajuste para o botão "Modificar" dos Relatórios (custom link) ---
    // Seleciona o botão "Modificar" que tem o href começando com "/concessoes/"
    const modificarRelatoriosButton = document.querySelector('a.changelink[href^="/concessoes/"]');

    if (modificarRelatoriosButton) {
        modificarRelatoriosButton.textContent = 'Visualizar'; // Altera para 'Visualizar'
    }

    // --- Ajuste para o texto "Dashboard" no menu lateral ---
    // Seleciona a tag <p> dentro do link do Dashboard (menu lateral)
    const dashboardTextElement = document.querySelector('a.nav-link[href="/admin/"] p'); 

    if (dashboardTextElement) {
        dashboardTextElement.textContent = 'Início'; // Altera para 'Início'
    }

    // --- Ajuste para o título <h1> "Dashboard" na página ---
    const dashboardTitleElement = document.querySelector('h1.h4.m-0.pr-3.mr-3.border-right');

    if (dashboardTitleElement && dashboardTitleElement.textContent.trim() === 'Dashboard') {
        dashboardTitleElement.textContent = 'Visão Geral'; // Altera para 'Visão Geral'
    }

    // --- Ajuste para o item do breadcrumb <li> "Dashboard" ---
    const breadcrumbDashboardItem = document.querySelector('.breadcrumb .breadcrumb-item:last-child');

    if (breadcrumbDashboardItem && breadcrumbDashboardItem.textContent.trim() === 'Dashboard') {
        breadcrumbDashboardItem.textContent = 'Visão Geral'; // onde altera o texto
    }

     // --- Ajuste para a mensagem de agradecimento ---
    // Seleciona o parágrafo com a classe 'text-center'
    const thankYouMessageElement = document.querySelector('p.text-center');

    // Verifica se o elemento foi encontrado E se o texto original corresponde ao esperado
    // Isso é uma proteção para não mudar outros parágrafos com 'text-center'
    if (thankYouMessageElement && thankYouMessageElement.textContent.trim() === 'Thanks for spending some quality time with the Web site today.') {
        // Altera o texto interno do parágrafo
        thankYouMessageElement.textContent = 'Obrigado por utilizar nosso Sistema hoje!'; // Mude para a sua nova mensagem
    }


     // --- Forçar o link "Relatórios" a abrir em uma nova aba ---
    // Seleciona o link "Relatórios" usando sua URL (que é o 'concession_public_list' do Jazzmin)
    const relatoriosLink = document.querySelector('a[href="/concessoes/"]');

    if (relatoriosLink) {
        relatoriosLink.setAttribute('target', '_blank');
        // Boa prática de segurança ao usar target="_blank"
        relatoriosLink.setAttribute('rel', 'noopener noreferrer');
    }
    
    const relatoriosLink2 = document.querySelector('a.changelink[href^="/concessoes/"]');

    if (relatoriosLink2) {
        relatoriosLink2.setAttribute('target', '_blank');
        // Boa prática de segurança ao usar target="_blank"
        relatoriosLink2.setAttribute('rel', 'noopener noreferrer');
    }

}); 