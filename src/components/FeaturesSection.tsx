
import React from 'react';
import { 
  UserCircle, Package, Truck, Bell, 
  HeadphonesIcon, RotateCcw, Users, BarChart3, 
  CreditCard, Settings
} from 'lucide-react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

const features = [
  {
    title: "Авторизация",
    description: "Регистрация клиентов по номеру телефона через Telegram ID и безопасное взаимодействие с API.",
    icon: UserCircle
  },
  {
    title: "Оформление заказа",
    description: "Интерактивная форма с интеграцией API Ozon для автоматического получения информации о заказах.",
    icon: Package
  },
  {
    title: "Отслеживание",
    description: "Запрос статуса посылки и автоматические уведомления о смене статуса отправления.",
    icon: Truck
  },
  {
    title: "Уведомления",
    description: "Настройка шаблонов уведомлений и автоматическая рассылка сообщений о статусе заказов.",
    icon: Bell
  },
  {
    title: "Поддержка",
    description: "Возможность создания запроса на связь с оператором и встроенный чат с поддержкой.",
    icon: HeadphonesIcon
  },
  {
    title: "Возвраты",
    description: "Обработка возвратов и претензий с автоматической генерацией накладной для возврата.",
    icon: RotateCcw
  },
  {
    title: "Управление курьерами",
    description: "Авторизация курьеров, назначение заказов и геолокация для отслеживания местоположения.",
    icon: Users
  },
  {
    title: "Аналитика",
    description: "Сбор статистики по доставкам и выгрузка отчетов в формате CSV или Excel.",
    icon: BarChart3
  },
  {
    title: "Платежи",
    description: "Поддержка онлайн-оплаты доставки через Telegram и уведомления о поступлении оплаты.",
    icon: CreditCard
  },
  {
    title: "Администрирование",
    description: "Интерфейс управления для операторов и настройки тарифов, зон доставки.",
    icon: Settings
  }
];

const FeaturesSection = () => {
  return (
    <section id="features" className="section">
      <div className="container mx-auto">
        <h2 className="section-title">Возможности</h2>
        <p className="section-description">
          Наш бот предлагает широкий спектр функций для упрощения процесса доставки
          и улучшения взаимодействия с клиентами.
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => (
            <Card key={index} className="bg-card border-border">
              <CardHeader className="pb-2">
                <feature.icon className="h-10 w-10 text-primary mb-2" />
                <CardTitle>{feature.title}</CardTitle>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-foreground/80 text-sm">
                  {feature.description}
                </CardDescription>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeaturesSection;
