
import React from 'react';
import { Button } from "@/components/ui/button";

const DownloadSection = () => {
  return (
    <section className="section">
      <div className="container mx-auto text-center">
        <h2 className="section-title">Начать использовать</h2>
        <p className="section-description mb-10">
          Присоединяйтесь к нашему сервису доставки и упростите процесс получения посылок из Ozon 
          на территории ДНР, ЛНР и ХО
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Button className="primary-button">
            Открыть в Telegram
          </Button>
          <Button variant="outline">
            Связаться с нами
          </Button>
        </div>
      </div>
    </section>
  );
};

export default DownloadSection;
