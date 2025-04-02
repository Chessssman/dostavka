
import React from 'react';
import { Button } from "@/components/ui/button";

const HeroSection = () => {
  return (
    <section className="bg-background py-20 px-6 md:px-12 text-center">
      <div className="container mx-auto">
        <h1 className="text-4xl md:text-5xl font-bold mb-4 text-primary">+7Доставки</h1>
        <p className="text-xl md:text-2xl mb-10 max-w-3xl mx-auto">
          Телеграмм чат-бот для автоматизации доставки Ozon на территории ДНР, ЛНР, ХО
        </p>
        <Button className="primary-button text-lg">Начать использовать</Button>
      </div>
    </section>
  );
};

export default HeroSection;
