const wrapper = document.querySelector(".wrapper__container");
const search = document.querySelector(".search__input");
const URL_API = "http://127.0.0.1:8000/api/events/";

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

function showEvent(data) {
  data.forEach((event) => {
    const eventElement = document.createElement("div");

    eventElement.classList.add("wrapper__activity", "activity");

    eventElement.innerHTML = `
        <div class="activity__event event">
            <div class="event__image">
            <img src="images/${event.photo}" alt="event">
            </div>
            <div class="events__content content">
              <details class="content__details details">
                <summary class="details__title">${event.title}</summary>
                <p class="details__description">___________________________</p>
                <p class="details__materials_title">${event.materials}</p>
                <p class="details__materials">___________________________</p>
              </details>
              <p class="content__authors">___________________________</p>
              <p class="content__date_and_time">${event.date_time}</p>
              <p class="content__numbers_of_seats">${event.places}</p>
              <button class="content__sign_button sign_button">
                Записаться
              </button>
            </div>
          </div>
        `;
    wrapper.appendChild(eventElement);
  });
}

getEvents(URL_API);
