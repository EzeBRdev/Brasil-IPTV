
const channelsContainer = document.getElementById("channels");
const searchInput = document.getElementById("search");
const totalChannels = document.getElementById("total-canais");
const categoryButtons = document.querySelectorAll(".category");

let channels = [];
let selectedCategory = "Todos";

async function loadChannels() {
    try {
        const response = await fetch("dist/channels.json");

        if (!response.ok) {
            throw new Error("Não foi possível carregar os canais.");
        }

        channels = await response.json();

        if (!Array.isArray(channels)) {
            throw new Error("Formato inválido do catálogo.");
        }

        totalChannels.textContent = channels.length;
        renderChannels();

    } catch (error) {
        channelsContainer.innerHTML = `
            <div class="empty-state">
                <span>📡</span>
                <h3>Catálogo em preparação</h3>
                <p>Os canais serão exibidos quando o catálogo estiver disponível.</p>
            </div>
        `;

        totalChannels.textContent = "0";
        console.error(error);
    }
}

function renderChannels() {
    const search = searchInput.value
        .trim()
        .toLowerCase();

    const filtered = channels.filter(channel => {
        const name = (channel.name || "").toLowerCase();
        const category = channel.category || "";

        const matchesSearch = name.includes(search);

        const matchesCategory =
            selectedCategory === "Todos" ||
            category === selectedCategory;

        return matchesSearch && matchesCategory;
    });

    if (filtered.length === 0) {
        channelsContainer.innerHTML = `
            <div class="empty-state">
                <span>🔎</span>
                <h3>Nenhum canal encontrado</h3>
                <p>Tente outra pesquisa ou categoria.</p>
            </div>
        `;
        return;
    }

    channelsContainer.innerHTML = filtered.map(channel => `
        <article class="channel-card">
            <div class="channel-logo">
                ${channel.logo
                    ? `<img src="${escapeHTML(channel.logo)}"
                            alt="Logo de ${escapeHTML(channel.name)}">`
                    : "📺"}
            </div>

            <h3>${escapeHTML(channel.name || "Canal")}</h3>

            <p>${escapeHTML(channel.category || "Brasileiro")}</p>

            <span class="status">Fonte cadastrada</span>
        </article>
    `).join("");
}

function escapeHTML(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    })[character]);
}

searchInput.addEventListener("input", renderChannels);

categoryButtons.forEach(button => {
    button.addEventListener("click", () => {
        categoryButtons.forEach(item =>
            item.classList.remove("active")
        );

        button.classList.add("active");
        selectedCategory = button.dataset.category;

        renderChannels();
    });
});

loadChannels();
