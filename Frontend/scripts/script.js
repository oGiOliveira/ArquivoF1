
//modais
    /*base modal*/
    const btnOpen = document.getElementById("btnOpenModal");
    const btnClose = document.getElementById("btnCloseModal");
    const modals = document.querySelectorAll(".modal");

    /*abre modal*/
    document.querySelectorAll("[data-open-modal]").forEach(btn => {
        btn.addEventListener("click", () => {
        const modalId = btn.dataset.openModal;
        const modal = document.getElementById(modalId);

        if (modal) {
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
                btn.closest(".modal").classList.remove("ativo");
            })
        })
        //botao de retornar para o modal anterior
        document.querySelectorAll(".btnReturnModal").forEach(btn => {
            btn.addEventListener("click", () => {
                btn.closest(".modal").classList.remove("ativo");
            })
        })
        /*clicando fora fecha*/
        document.querySelectorAll(".modal").forEach(modal => {
            modal.addEventListener("click", e => {
                if (e.target === modal) {
                    modal.classList.remove("ativo");
                }
            });
        });
    //fim da funcionalidades de fechar os modais
