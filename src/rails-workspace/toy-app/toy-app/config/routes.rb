Rails.application.routes.draw do
  resources :microposts
  root "users#index"
  resources :users

  # root "application#hello"

end
