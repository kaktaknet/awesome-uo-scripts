using System;
using System.Collections;
using Server;
using Server.Items;
using Server.Network;
using Server.ContextMenus;
using Server.Spells;

namespace Server.Mobiles
{
	public class BaseRyan : BaseCreature
	{
		int m_price;

		public override bool Commandable{ get{ return false; } } // Our master cannot boss us around!

		[CommandProperty( AccessLevel.GameMaster )]
		public int Price
		{
			get{ return m_price;}
			set{ m_price = value;}
		}


		[Constructable]
		public BaseRyan() : base( AIType.AI_Melee, FightMode.Agressor, 22, 1, 0.2, 1.0 )
		{
			Title = "The Man Whore";
			Name = "Ryan McAdams";
			Body = 400;
			Hue = Utility.RandomSkinHue();
			InitBody();
			InitOutfit();
			m_price = Utility.Random(800);
			SetPrice();
			
		}


		


		public virtual void InitBody()
		{
			SetStr( 20, 30 );
			SetDex( 90, 100 );
			SetInt( 15, 25 );

			
			
		
		}

		public virtual void SetPrice()
		{
			m_price = Utility.Random( 800);
		}

		public virtual void InitOutfit()
		{
			AddItem( new FancyShirt( Utility.RandomNeutralHue() ) );
			AddItem( new ShortPants( Utility.RandomNeutralHue() ) );
			AddItem( new Boots( Utility.RandomNeutralHue() ) );

			switch ( Utility.Random( 2 ) )
			{
				case 0: AddItem( new ShortHair( Utility.RandomHairHue() ) ); break;
				case 1: AddItem( new ReceedingHair( Utility.RandomHairHue() ) ); break;
				
			}
			
			PackGold( 200, 250 );
		}
		
		public virtual bool SayPrice()
		{
				Say( "I'll suck your dick for {0} gold", m_price );
				return true;
		}
		
		public virtual bool SaySomething(String s )
		{
				Say( "{0}", s );
				return true;
		}

		public virtual int GetPrice()
		{
				return m_price;
		}

		private static TimeSpan m_EscortDelay = TimeSpan.FromMinutes( 5.0 );

		public override void OnThink()
		{
			base.OnThink();
		}

		private DateTime m_LastSeenEscorter;


		public BaseRyan( Serial serial ) : base( serial )
		{
		}

		public override void Serialize( GenericWriter writer )
		{
			base.Serialize( writer );

			writer.Write( (int) 0 ); // version

		}

		public override void Deserialize( GenericReader reader )
		{
			base.Deserialize( reader );

			int version = reader.ReadInt();

		}

		public override bool CanBeRenamedBy( Mobile from )
		{
			return ( from.AccessLevel >= AccessLevel.GameMaster );
		}

		public override void AddCustomContextEntries( Mobile from, ArrayList list )
		{
				//Mobile escorter = GetEscorter();

					list.Add( new AskRyanPrice( this, from ) );
					list.Add( new PayForRyan( this, from));

			base.AddCustomContextEntries( from, list );
		}



	}

	public class AskRyanPrice: ContextMenuEntry
	{
		private BaseRyan m_Mobile;
		private Mobile m_From;

		public AskRyanPrice( BaseRyan m, Mobile from ) : base( 0377, 3 )
		{
			m_Mobile = m;
			m_From = from;
		}

		public override void OnClick()
		{
			m_Mobile.SayPrice( );
		}
	}


	public class PayForRyan : ContextMenuEntry
	{
		private BaseRyan m_Mobile;
		private Mobile m_From;
		Container cont;

		public PayForRyan ( BaseRyan m, Mobile from ) : base( 6101, 3 )
		{
			m_Mobile = m;
			m_From = from;
		}

		public override void OnClick()
		{
			cont = m_From.Backpack;

			if ( cont.ConsumeTotal( typeof( Gold ), m_Mobile.GetPrice() ) ){
				m_Mobile.SaySomething( "Oh yea, I love the cock!" );
				Misc.Titles.AwardFame( m_From, 10, true );
				m_From.Animate( 23, 5, 1, true, true, 0 ); 
				SpellHelper.AddStatBonus( m_From, m_From, StatType.Str, 5, TimeSpan.FromMinutes( 1.3 )); SpellHelper.DisableSkillCheck = true;
				SpellHelper.AddStatBonus( m_From, m_From, StatType.Dex, 5, TimeSpan.FromMinutes( 1.3 )); 
				SpellHelper.AddStatBonus( m_From, m_From, StatType.Int, 5, TimeSpan.FromMinutes( 1.3 )); SpellHelper.DisableSkillCheck = false;


			} else {
				m_Mobile.SaySomething( "I'm a money grubbing whore. Give me more money." );
			}

		}
	}





}