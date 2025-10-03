"""Specialized risk models for different market asset types."""
from typing import Optional, Union
from pydantic import BaseModel, Field


class BaseFincoreKeyRisks(BaseModel):
    """Base class for all market-specific risk models."""
    regulatory_risks: str = Field(..., description="Regulatory risks affecting the asset, such as legal changes, compliance")
    macroeconomic_risks: str = Field(..., description="Macroeconomic risks, such as interest rates, inflation")
    political_and_geopolitical_risks: str = Field(..., description="Political and geopolitical risks, such as tariffs, wars, elections")
    climate_and_environmental_risks: str = Field(..., description="Climate and environmental risks, such as natural disasters, resource scarcity")


class StockKeyRisks(BaseFincoreKeyRisks):
    """Risk model specifically for stock/equity investments."""
    competitive_risks: str = Field(..., description="Competitive risks in the sector/industry, such as new entrants, innovation disruptions")
    operational_execution_risks: str = Field(..., description="Company operational execution risks, such as supply chain, production issues")
    management_risks: str = Field(..., description="Management and leadership risks, such as CEO image, governance, strategy")
    financial_risks: str = Field(..., description="Financial risks, such as earnings volatility and guidance risks, debt levels")
    sector_specific_risks: str = Field(..., description="Industry/sector-specific risks, such as regulatory changes, commodity price exposure")
    contract_and_ownership_type_risks: Optional[str] = Field(None, description="Risks specific to contract or ownership type, e.g., SPOT, FUTURE, OPTION")


class CryptoKeyRisks(BaseFincoreKeyRisks):
    """Risk model specifically for cryptocurrency investments."""
    adoption_risks: str = Field(..., description="Market adoption and network effect risks, including user growth and developer activity")
    security_risks: str = Field(..., description="Security vulnerabilities and hacking risks, including smart contract risks")
    volatility_risks: str = Field(..., description="Extreme price volatility risks, including liquidity and market manipulation")
    liquidity_risks: str = Field(..., description="Market liquidity and exchange risks, including delistings and exchange hacks")


class CommodityKeyRisks(BaseFincoreKeyRisks):
    """Risk model specifically for commodity investments."""
    supply_demand_imbalance_risks: str = Field(..., description="Supply and demand imbalance risks, including geopolitical tensions and trade policies")
    producer_risks: str = Field(..., description="Major producer and supplier concentration risks, including OPEC dynamics and mining regulations")
    substitute_risks: str = Field(..., description="Substitute products and alternatives risks, including renewable energy sources and synthetic materials")
    inventory_risks: str = Field(..., description="Global inventory levels and stockpile risks, including strategic reserves and seasonal fluctuations")


class ETFKeyRisks(BaseFincoreKeyRisks):
    """Risk model specifically for ETF (Exchange-Traded Fund) investments."""
    counterparty_risks: str = Field(..., description="Counterparty and issuer risks, including fund sponsor stability and credit risks")
    management_risks: str = Field(..., description="Fund management and operational risks, including tracking error and expense management")
    expense_and_fees_risks: str = Field(..., description="Fee structure and expense impact risks, including hidden costs and tax inefficiencies")
    closure_risks: Optional[str] = Field(None, description="ETF closure or merger risks, including liquidity and redemption issues")


# Union type for all market-specific risk models
MarketKeyRisks = Union[StockKeyRisks, CryptoKeyRisks, CommodityKeyRisks, ETFKeyRisks, BaseFincoreKeyRisks]