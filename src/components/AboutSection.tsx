
import React from 'react';

const AboutSection = () => {
  return (
    <section id="about" className="section bg-card">
      <div className="container mx-auto">
        <h2 className="section-title">О боте</h2>
        <p className="section-description">
          Чат-бот +7Доставки предназначен для автоматизации обработки заказов, отслеживания посылок 
          и взаимодействия с клиентами. Бот интегрирован с CRM, API Ozon и системой логистики 
          ООО «Айси-Транс» для обеспечения быстрой и надежной доставки на территории ДНР, ЛНР и ХО.
        </p>
      </div>
    </section>
  );
};

export default AboutSection;
