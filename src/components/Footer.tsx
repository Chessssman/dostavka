
import React from 'react';
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="bg-card py-10 px-6">
      <div className="container mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          <div>
            <h3 className="text-lg font-bold mb-4">+7Доставки</h3>
            <p className="text-sm text-muted-foreground">
              Доставка Ozon на территории ДНР, ЛНР, ХО.<br />
              ООО «Айси-Транс»
            </p>
          </div>
          
          <div>
            <h3 className="text-lg font-bold mb-4">Навигация</h3>
            <ul className="space-y-2">
              <li><Link to="/" className="text-sm text-muted-foreground hover:text-primary">Главная</Link></li>
              <li><Link to="#about" className="text-sm text-muted-foreground hover:text-primary">О боте</Link></li>
              <li><Link to="#features" className="text-sm text-muted-foreground hover:text-primary">Возможности</Link></li>
              <li><Link to="#tech" className="text-sm text-muted-foreground hover:text-primary">Технологии</Link></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-lg font-bold mb-4">Контакты</h3>
            <ul className="space-y-2">
              <li className="text-sm text-muted-foreground">Телефон: +7 (XXX) XXX-XX-XX</li>
              <li className="text-sm text-muted-foreground">Email: info@7delivery.ru</li>
              <li className="text-sm text-muted-foreground">Telegram: @SevenDeliveryBot</li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-border mt-10 pt-6 text-center">
          <p className="text-sm text-muted-foreground">
            © 2023 +7Доставки. ООО «Айси-Транс». Все права защищены.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
