
import React from 'react';
import { Badge } from "@/components/ui/badge";

const technologies = [
  "Python", "Aiogram", "FastAPI", "PostgreSQL", 
  "API Ozon", "CRM", "Telegram Bot API", "SQLite",
  "Docker", "Git", "CI/CD"
];

const TechSection = () => {
  return (
    <section id="tech" className="section bg-card">
      <div className="container mx-auto">
        <h2 className="section-title">Технические особенности</h2>
        <p className="section-description">
          Проект разработан с использованием современных технологий для обеспечения 
          надежной и быстрой работы системы доставки
        </p>
        
        <div className="flex flex-wrap justify-center gap-3 mb-10">
          {technologies.map((tech, index) => (
            <Badge key={index} variant="secondary" className="text-base py-2 px-4">
              {tech}
            </Badge>
          ))}
        </div>
        
        <div className="max-w-3xl mx-auto bg-secondary rounded-lg p-6">
          <h3 className="text-xl font-semibold mb-4">Основные преимущества</h3>
          <ul className="space-y-3">
            <li className="flex items-start">
              <span className="text-primary mr-2">•</span>
              <span>Интеграция с API Ozon для автоматического получения данных о заказах</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary mr-2">•</span>
              <span>Разработка на основе Aiogram для стабильной работы Telegram бота</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary mr-2">•</span>
              <span>Использование FastAPI для быстрой обработки запросов</span>
            </li>
            <li className="flex items-start">
              <span className="text-primary mr-2">•</span>
              <span>Надежное хранение данных в PostgreSQL с резервным копированием</span>
            </li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default TechSection;
