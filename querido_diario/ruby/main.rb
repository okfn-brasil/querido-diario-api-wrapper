# frozen_string_literal: true

require 'bundler/inline'

gemfile do
  source 'https://rubygems.org'
  gem 'pry'
  gem 'faraday', '~> 1.8'
  gem 'faraday_middleware', '~> 1.1'
end

require 'faraday'
require 'faraday_middleware'
require_relative 'territories'

module QueridoDiario
  module_function

  BASE_API_URL = 'https://queridodiario.ok.org.br/api/'

  CONN = Faraday.new do |f|
    f.request :json
    f.request :retry
    f.response :follow_redirects
    f.response :json
    f.options[:params_encoder] = Faraday::FlatParamsEncoder
  end

  def gazettes(args)
    request = base_gazettes(**args)
    request.success? ? request.body : request.status
  end

  def base_gazettes(since: nil, up_to: nil, keywords: nil, territory_id: nil, offset: 0, size: 10)
    endpoint = territory_id ? "gazettes/#{territory_id}" : 'gazettes/'

    payload = [
      "offset=#{offset}",
      "size=#{size}"
    ]

    payload.push("since=#{since}") unless since.nil?
    payload.push("until=#{up_to}") unless up_to.nil?
    keywords.each { |keyword| payload.push("keywords=#{keyword}") }

    url_params = payload.join('&')

    CONN.get("#{BASE_API_URL}#{endpoint}?#{url_params}")
  end

  def territories
    Territories::ALL
  end
end
