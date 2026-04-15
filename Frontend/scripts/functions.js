//pop-up de feedback é aqui
function showPopup(message) {
    let popup = document.createElement('div');
    popup.className = 'quickPopup';
    popup.textContent = message;
    document.body.appendChild(popup);
    setTimeout(() => popup.remove(), 2000);
}
//fim pop-ups


/*pop-up success driver register*/
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('modalDriver');
    if (form) {
        form.addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(form);
            const response = await fetch(form.action, {
                method: 'POST', 
                headers: {
                    'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                body: formData
            });
            if (response.ok) {

                const data = await response.json();
                const pilotoNome = formData.get("nameDriver");
                const pilotoEquipe = formData.get("team");
                const pilotoDataNasc = formData.get("dateDriver");
                const pilotoNumeracao = formData.get("numberDriver");
                const pilotoPais = formData.get("country");
                const pilotoFoto = formData.get("imageDriver");

                criarBoxTransferencia(pilotoNome, pilotoEquipe, pilotoDataNasc, pilotoNumeracao, pilotoPais, pilotoFoto, data.id);
                showPopup('Cadastro de piloto registrado com sucesso!');
                form.reset();

                resetDriverForm();
            }
            else
            {
                showPopup('Erro ao registrar o piloto!');
            }
        });
    }
});



//function clean para limpar os campos do forms
function resetDriverForm() {
    //removendo modal
    document.getElementById('modalDriverWizard step active').classList.remove('ativo');

    //limpando campos do form
    document.querySelector('.nameDriverInput').value = '';
    document.getElementById('team').value = '';
    document.querySelector('.dateDriverInput').value = '';

    //limpando campos ocultos
    document.getElementById('hiddenTypeRegister').value = '';
    document.getElementById('hiddenNameDriver').value = '';
    document.getElementById('hiddenTeamDriver').value = '';
    document.getElementById('hiddenDateDriver').value = '';
    document.getElementById('hiddenDateDriver').value = '';
}
//fim function clean para limpar os campos do forms

    
