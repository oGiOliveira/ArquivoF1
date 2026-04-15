/*botao dropdown*/
function toggleDropdown(id) {
    const box = document.getElementById("opcoes-" + id);
    box.style.display = (box.style.display === "flex") ? "none" : "flex";
}

function selecionar(valor, id) {
    if (id === 'a') {
        document.getElementById("team").innerText = valor;
    }
    else if (id === 'b') {
        document.getElementById("country").innerText = valor;
    }
    document.getElementById("opcoes-" + id).style.display = "none";
}

document.addEventListener("click", function(event) {
    const dropdown = document.querySelectorAll(".dropdownOptions");
    dropdown.forEach(menu => {
        if (!menu.contains(event.target) && !event.target.closest(".dropdownInput")){
            menu.style.display = "none";
        }
    });
});
/*fim botao dropdown*/

//modais
    /*base modal*/
    const btnOpen = document.getElementById("btnOpenModal");
    const btnClose = document.getElementById("btnCloseModal");

    const modals = document.querySelectorAll(".modalType, .modalForm");

    /*abre modal*/
    document.querySelectorAll("[data-open-modal]").forEach(btn => {
        btn.addEventListener("click", () => {
        const modalId = btn.dataset.openModal;
        const modal = document.getElementById(modalId);
            
        if (modal) {
            //fecha modais abertos
            modals.forEach(m => m.classList.remove("ativo"));
            //abre modal
            modal.classList.add("ativo");
        }
        else
        {
            //erro se nao encontrar
            console.error(`Modal com ID "${modalId}" não encontrado.`);
        }
        });
    });
    /*fim da base modal*/

    //funcionalidades de fechar os modais
        /*botaoa X que fecha qualquer modal*/
        document.querySelectorAll(".btnCloseModal").forEach(btn => {
            btn.addEventListener("click", () => {
                btn.closest(".modalType, .modalForm").classList.remove("ativo");
            })
        })
        //botao de retornar para o modal anterior
        document.querySelectorAll(".btnReturnModal").forEach(btn => {
            btn.addEventListener("click", () => {
                btn.closest(".modalType, .modalForm").classList.remove("ativo");
            })
        })
        /*clicando fora fecha*/
        document.querySelectorAll(".modalType, .modalForm").forEach(modal => {
            modal.addEventListener("click", e => {
                if (e.target === modal) {
                    modal.classList.remove("ativo");
                }
            });
        });
    //fim da funcionalidades de fechar os modais

//funcionalidade de menu wizard (passar pro proximo menu)
document.querySelectorAll(".modalForm").forEach(modal => {
    const wizard = modal.querySelector('.wizard');
    if (!wizard) return;

    const steps = wizard.querySelectorAll(".step");
    const tabs = wizard.querySelectorAll(".tab");
    let currentStep = 0;

    function showStep(index) {
        steps.forEach((step, i) => {
            step.classList.remove("active");
            if (i === index) {
                step.classList.add("active");
            }
        });
        tabs.forEach((tabs, i) => {
            tabs.classList.remove("active");
            if (i === index) {
                tabs.classList.add("active");
            }
        });

        currentStep = index;
    }

    //clique para mudar de aba
    tabs.forEach(tab => {
        tab.addEventListener("click", () => {
            const stepIndex = parseInt(tab.dataset.setp);
            showStep(stepIndex);
        });
    })

    //botao de prosseguir
    wizard.querySelectorAll(".nextBtn").forEach(btn => {
        btn.addEventListener("click", () => {
            if (currentStep < steps.length - 1) {
                currentStep++;
                showStep(currentStep);
            }
        });
    });
});