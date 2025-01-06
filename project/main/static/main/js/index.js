const wrapper = document.querySelector(".wrapper__activity");
const form = document.querySelector(".search__form");
const search = document.querySelector(".search__input");
const modalWindow = document.querySelector(".modal");

const URL_API = "http://127.0.0.1:8000/api/events/";

// Функция для получения всех событий
async function getEvents(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Ошибка HTTP: ${response.status}`);
    }

    const respData = await response.json();
    console.log(respData);
    showEvent(respData);
  } catch (error) {
    console.error("Ошибка при получении данных:", error);
  }
}

// Функция для отображения всех событий
// Функция для отображения всех событий
function showEvent(data) {
  data.forEach((event) => {
    const eventElement = document.createElement("div");

    eventElement.classList.add("activity__event", "event");

    eventElement.innerHTML = `
  ${
    event.photo
      ? `<div class="event__container_image">
          <img src="${event.photo}" alt="event" class="event__image" id="image">
        </div>`
      : ""
  }
  <div class="events__content content">
    <details class="content__details details">
      <summary class="details__title">${event.title}</summary>
      <p class="details__description">${event.description}</p>
      <p class="details__materials_title"></p>
      <p class="details__materials">${event.materials}</p>
    </details>
    <p class="content__authors">${event.author}</p>
    <p class="content__date_and_time">${event.date_time
      .replace("T", " ")
      .replace("Z", " ")
      .replace("-", ".")
      .replace("-", ".")}</p>
    <p class="content__numbers_of_seats">Количество мест: ${
      event.available_seats
    }</p>
    <button class="content__sign_button sign_button" data-event-id="${
      event.id
    }">
      Записаться
    </button>
  </div>
`;

    const signButton = eventElement.querySelector(".content__sign_button");
    signButton.addEventListener("click", async (e) => {
      const eventId = e.target.getAttribute("data-event-id");
      openModal(eventId);
      btn_close = document.querySelector(".modal__button");
      btn_close.addEventListener("click", () => {
        closeModal();
      });
      const displayClose = document.querySelector(".modal--show");
      displayClose.addEventListener("click", (e) => {
        if (e.target.className == "modal modal--show") {
          closeModal();
        }
      });
      // // Отправка запроса на регистрацию
      // const response = await fetch(`/api/register_event/${eventId}/`, {
      //   method: "POST",
      //   headers: {
      //     "Content-Type": "application/json",
      //     "X-CSRFToken": getCookie("csrftoken"), // Используйте CSRF-токен, если нужно
      //   },
      // });
      // const result = await response.json();

      // if (response.ok) {
      //   alert(result.message);
      //   // Обновляем количество доступных мест на странице
      //   e.target
      //     .closest(".event")
      //     .querySelector(
      //       ".content__numbers_of_seats"
      //     ).textContent = `Количество мест: ${result.available_seats}`;
      // } else {
      //   alert(result.error);
      // }
    });

    wrapper.appendChild(eventElement);
  });
}

// Функция для получения CSRF токена
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Обработчик отправки формы
form.addEventListener("submit", (event) => {
  event.preventDefault();
  searchEvents();
  // console.log(search.value);
});

// Функция для поиска событий
async function searchEvents() {
  // console.log("Поиск...");
  if (search.value) {
    const apiUrl = `http://127.0.0.1:8000/api/events/?search=${encodeURIComponent(
      search.value
    )}`;
    // console.log(`URL для поиска: ${apiUrl}`);

    try {
      const response = await fetch(apiUrl);

      if (!response.ok) {
        throw new Error(`Ошибка: ${response.status}`);
      }

      const data = await response.json();
      // console.log("Полученные данные для поиска:", data);
      showSearchEvents(data);
    } catch (error) {
      console.error("Ошибка при получении данных:", error);
    }
  }
}

function showSearchEvents(data) {
  wrapper.innerHTML = ""; // Очистить текущие события
  showEvent(data); // Отобразить новые события
}
// -------------------модалка--------------
function openModal(id) {
  modalWindow.classList.add("modal--show");
  document.body.classList.add("stop-scroling");
  modalWindow.innerHTML = `
  <div class="modal__card">
      <h2 class="modal__title">Выбрать дату и время</h2>
      <button class="modal__button">закрыть</button>
    </div>       
  `;
}
function closeModal() {
  modalWindow.classList.remove("modal--show");
  document.body.classList.remove("stop-scroling");
}
//-------------------------------------------
// Получить все события при загрузке страницы
getEvents(URL_API);
